function cleanSet(set, startString) {
    if (startString === "") return ""
    const cleaned = [...set].filter(item => item.startsWith(startString)).map(item => item.slice(startString.length)).join("-")
    return cleaned
}

export default cleanSet;
