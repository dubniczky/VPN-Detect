const API_KEY = '...'
const IP_URL = `https://api.ipgetlocation.io/getip`
const LOC_URL = `https://api.ipgetlocation.io/ipgeo?api_key=${API_KEY}&ip=`

function getRealLocation() {
    return Intl.DateTimeFormat().resolvedOptions().timeZone
}

async function fetchJson(url) {
    return await (await fetch(url)).json()
}

async function getSimulatedLocation() {
    const ip = (await fetchJson(IP_URL)).ip
    return (await fetchJson(LOC_URL + ip)).time_zone.name
}

async function detectVPN() {
    const real = getRealLocation()
    const simulated = await getSimulatedLocation()
    return {
        vpn: real == simulated,
        real,
        simulated
    }
}