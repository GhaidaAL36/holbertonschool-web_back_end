function updateStudentGradeByCity(array, city, newGrades = []) {
    const result = array
        .filter(objs => objs.location === city)
        .map(objs => {
            const gradeValue = newGrades.find(grade => grade.studentId === objs.id);
            return {
                id: objs.id,
                firstName: objs.firstName,
                location: objs.location,
                grade: gradeValue ? gradeValue.grade : "N/A"
            };
        });
    return result;
}

export default updateStudentGradeByCity;
