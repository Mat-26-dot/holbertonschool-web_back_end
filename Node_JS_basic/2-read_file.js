const fs = require('fs');

function countStudents(path) {
  try {
    // Read the file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split into lines and filter out empty lines
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Remove the header line (first line)
    const studentLines = lines.slice(1);

    // Filter out any remaining empty lines
    const validStudents = studentLines.filter((line) => line.trim() !== '');

    if (validStudents.length === 0) {
      console.log('Number of students: 0');
      return;
    }

    // Parse student data
    const students = validStudents.map((line) => {
      const [firstname, lastname, age, field] = line.split(',');
      return {
        firstname: firstname ? firstname.trim() : '',
        lastname: lastname ? lastname.trim() : '',
        age: age ? age.trim() : '',
        field: field ? field.trim() : ''
      };
    });

    // Group students by field
    const fieldGroups = {};
    students.forEach((student) => {
      if (student.field && student.firstname) {
        if (!fieldGroups[student.field]) {
          fieldGroups[student.field] = [];
        }
        fieldGroups[student.field].push(student.firstname);
      }
    });

    // Log total number of students
    console.log(`Number of students: ${students.length}`);

    // Log students by field
    Object.keys(fieldGroups).forEach((field) => {
      const studentList = fieldGroups[field];
      console.log(`Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`);
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;