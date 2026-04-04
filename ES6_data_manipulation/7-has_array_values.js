function hasValuesFromArray(set, array) {
    const hasValues = array.every(val => set.has(val))
    return hasValues
}

export default hasValuesFromArray;
