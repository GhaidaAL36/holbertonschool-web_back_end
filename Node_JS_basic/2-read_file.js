const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const line = data.split('\n');
    const rows = line.slice(1).filter((row) => row.trim() !== '' && row.split(',').length === 4);

    const fields = {};
    rows.forEach((row) => {
      const colums = row.split(',');
      const firstName = colums[0].trim();
      const field = colums[3].trim();

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    });

    console.log(`Number of students: ${rows.length}`);
    for (const [field, students] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
