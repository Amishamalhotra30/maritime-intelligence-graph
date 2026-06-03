import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

const data = [
  {
    region: "Middle East",
    score: 30
  },
  {
    region: "Far East",
    score: -10
  },
  {
    region: "North Africa",
    score: -15
  }
];

function OpportunityChart() {
  return (
    <div
      className="card"
      style={{
        width: "100%",
        marginTop: "30px"
      }}
    >
      <h2>Opportunity Scores</h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >
        <BarChart data={data}>
          <XAxis dataKey="region" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="score" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default OpportunityChart;