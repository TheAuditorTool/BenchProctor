const express = require("express");
const session = require("express-session");

const scoreAnomaly = require("./anomaly_score").scoreAnomaly;
const renderCheckpoint = require("./render_checkpoint").renderCheckpoint;
const buildBundle = require("./build_bundle").buildBundle;
const validateBundle = require("./validate_bundle").validateBundle;
const resolveBundle = require("./resolve_bundle").resolveBundle;
const enrichConfig = require("./enrich_config").enrichConfig;
const mergeDigest = require("./merge_digest").mergeDigest;
const resolveReport = require("./resolve_report").resolveReport;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/scoreAnomaly", route(scoreAnomaly));
app.post("/renderCheckpoint", route(renderCheckpoint));
app.post("/buildBundle", route(buildBundle));
app.post("/validateBundle", route(validateBundle));
app.post("/resolveBundle", route(resolveBundle));
app.post("/enrichConfig", route(enrichConfig));
app.post("/mergeDigest", route(mergeDigest));
app.post("/resolveReport", route(resolveReport));

app.listen(3000, "0.0.0.0");
