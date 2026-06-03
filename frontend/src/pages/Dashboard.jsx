import KPI from "../components/KPI";
import OpportunityChart from "../components/OpportunityChart";
import CargoTable from "../components/CargoTable";
import VesselTable from "../components/VesselTable";

function Dashboard() {
  return (
    <>
      <h1 className="title">
        Maritime Intelligence Graph 
      </h1>

      <div className="kpi-container">
        <KPI title="Cargoes" value="3" />
        <KPI title="Open Vessels" value="5" />
        <KPI title="Brokers" value="1" />
        <KPI title="Emails" value="15" />
        <KPI title="Trade Lanes" value="3" />
        <KPI title="Graph Nodes" value="19" />
      </div>

      <div className="snapshot-card">
        <h2>Market Snapshot</h2>

        <p>
          <b>Top Opportunity:</b>
          Middle East → Europe
        </p>

        <p>
          <b>Cargo Rich Region:</b>
          Middle East
        </p>

        <p>
          <b>Vessel Rich Region:</b>
          North Africa
        </p>

        <p>
          <b>Top Broker:</b>
          LIDOMAR
        </p>
        <h2>Pipeline Summary</h2>

   <div className="pipeline-grid">

    <div>
      <h3>VC Emails</h3>
      <p>4</p>
    </div>

    <div>
      <h3>TC Emails</h3>
      <p>5</p>
    </div>

    <div>
      <h3>Tonnage Emails</h3>
      <p>6</p>
    </div>

    <div>
      <h3>Cargoes</h3>
      <p>3</p>
    </div>

    <div>
      <h3>Vessels</h3>
      <p>5</p>
    </div>

    <div>
      <h3>Brokers</h3>
      <p>1</p>
    </div>

  </div>

      </div>

      <OpportunityChart />

      <CargoTable />
      <VesselTable />
    </>
  );
}

export default Dashboard;