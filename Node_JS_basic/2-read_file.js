const fs = require('fs');

function countStudents(path) {
    try {
        // Read file synchronously with UTF-8 encoding
        const data = fs.readFileSync(path, 'utf8');

        // Split into lines and filter out empty lines (not valid students)
        const validLines = data.split('\n').filter(line => line.trim().length > 0);

        // If no valid lines or only header line exists
        if (validLines.length <= 1) {
            console.log('Number of students: 0');
            return;
        }

        // Extract header (first line) and data lines (remaining lines)
        const headerLine = validLines[0];
        const dataLines = validLines.slice(1);

        // Parse header to get column names
        const headers = headerLine.split(',').map(header => header.trim());

        // Parse student data
        const students = [];

        for (const line of dataLines) {
            const fields = line.split(',').map(field => field.trim());

            // Only process lines that have the correct number of fields
            // and have a non-empty first field (firstname)
            if (fields.length === headers.length && fields[0] && fields[0] !== '') {
                const student = {};

                // Map each field to its corresponding header
                for (let i = 0; i < headers.length; i++) {
                    student[headers[i]] = fields[i];
                }

                students.push(student);
            }
        }

        // Log the total number of students
        console.log(`Number of students: ${students.length}`);

        // If no valid students found, return early
        if (students.length === 0) {
            return;
        }

        // Group students by field and collect first names
        const fieldGroups = {};

        students.forEach(student => {
            // Get the field of study and firstname
            const field = student.field;
            const firstname = student.firstname;

            if (field && firstname) {
                if (!fieldGroups[field]) {
                    fieldGroups[field] = [];
                }
                fieldGroups[field].push(firstname);
            }
        });

        // Log the number of students in each field with the required format
        // Sort fields alphabetically for consistent output
        const sortedFields = Object.keys(fieldGroups).sort();

        for (const field of sortedFields) {
            const names = fieldGroups[field];
            console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }

    } catch (error) {
        if (error.code === 'ENOENT') {
            throw new Error('Cannot load the database');
        }
        throw error;
    }
}

module.exports = countStudents;