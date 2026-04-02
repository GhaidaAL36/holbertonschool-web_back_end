function getStudentsByLocation(array, city) {
    if (!Array.isArray(array)) return [];
    return array.filter(objects => objects.location === city)
}

export default getStudentsByLocation;
