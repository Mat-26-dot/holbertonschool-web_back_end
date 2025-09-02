const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      try {
        // Split the data into lines and filter out empty lines
        const lines = data.split('\n').filter(line => line.trim() !== '');
        
        // Remove the header line (first line)
        const studentLines = lines.slice(1);
        
        // Filter out any remaining empty lines
        const validStudents = studentLines.filter(line => line.trim() !== '');
        
        // Parse student data
        const students = validStudents.map(line => {
          const [firstname, lastname, age, field] = line.split(',');
          return { firstname: firstname.trim(), lastname: lastname.trim(), age: age.trim(), field: field.trim() };
        });

        // Log total number of students
        console.log(`Number of students: ${students.length}`);

        // Group students by field
        const fieldGroups = {};
        students.forEach(student => {
          if (!fieldGroups[student.field]) {
            fieldGroups[student.field] = [];
          }
          fieldGroups[student.field].push(student.firstname);
        });

        // Log students by field
        Object.keys(fieldGroups).forEach(field => {
          const studentList = fieldGroups[field];
          console.log(`Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`);
        });

        resolve();
      } catch (parseError) {
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

module.exports = countStudents;