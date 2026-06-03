import { useEffect, useState } from "react";

function VesselTable() {

  const [vessels, setVessels] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/vessels")
      .then((res) => res.json())
      .then((data) => setVessels(data))
      .catch((err) => console.error(err));

  }, []);

  return (

    <div className="table-card">

      <h2>Recent Open Vessels</h2>

      <table>

        <thead>

          <tr>
            <th>Vessel</th>
            <th>Size</th>
            <th>Open Port</th>
            <th>Open Date</th>
          </tr>

        </thead>

        <tbody>

          {vessels.map((vessel, index) => (

            <tr key={index}>

              <td>
                {vessel.vessel_name || "-"}
              </td>

              <td>
                {vessel.vessel_size || "-"}
              </td>

              <td>
                {vessel.open_port || "-"}
              </td>

              <td>
                {vessel.open_date || "-"}
              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>

  );
}

export default VesselTable;