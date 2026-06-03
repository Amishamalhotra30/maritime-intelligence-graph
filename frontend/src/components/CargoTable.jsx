import { useEffect, useState } from "react";

function CargoTable() {

  const [cargoes, setCargoes] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/cargoes")
      .then((res) => res.json())
      .then((data) => setCargoes(data))
      .catch((err) => console.error(err));

  }, []);

  return (

    <div className="table-card">

      <h2>Recent Cargo Opportunities</h2>

      <table>

        <thead>
          <tr>
            <th>Cargo</th>
            <th>Load Port</th>
            <th>Discharge Port</th>
            <th>Broker</th>
          </tr>
        </thead>

        <tbody>

          {cargoes.map((cargo, index) => (

            <tr key={index}>

              <td>{cargo.cargo_name}</td>
              <td>{cargo.loading_port}</td>
              <td>{cargo.discharge_port}</td>
              <td>{cargo.broker || "N/A"}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default CargoTable;