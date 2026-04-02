function getStudentIdsSum(array) {
    return array.reduce((total, obj) => total += obj.id, 0)
}

export default getStudentIdsSum;
