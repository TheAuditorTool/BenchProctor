const express = require("express");
const session = require("express-session");

const ingestMetric = require("./metric_ingest").ingestMetric;
const auditSchedule = require("./audit_schedule").auditSchedule;
const pruneBatch = require("./prune_batch").pruneBatch;
const exportAlert = require("./export_alert").exportAlert;
const renderManifest = require("./render_manifest").renderManifest;
const formatSchedule = require("./format_schedule").formatSchedule;
const annotateDigest = require("./annotate_digest").annotateDigest;
const exportSchedule = require("./export_schedule").exportSchedule;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/ingestMetric", ingestMetric);
app.post("/auditSchedule", auditSchedule);
app.post("/pruneBatch", pruneBatch);
app.post("/exportAlert", exportAlert);
app.post("/renderManifest", renderManifest);
app.post("/formatSchedule", formatSchedule);
app.post("/annotateDigest", annotateDigest);
app.post("/exportSchedule", exportSchedule);

app.listen(3000, "0.0.0.0");
