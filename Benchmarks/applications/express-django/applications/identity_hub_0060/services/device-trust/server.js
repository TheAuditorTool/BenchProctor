const express = require("express");
const session = require("express-session");

const enrollDevice = require("./device_enroll").enrollDevice;
const summarizeIndex = require("./summarize_index").summarizeIndex;
const annotateProfile = require("./annotate_profile").annotateProfile;
const summarizePolicy = require("./summarize_policy").summarizePolicy;
const exportSummary = require("./export_summary").exportSummary;
const reconcileSummary = require("./reconcile_summary").reconcileSummary;
const renderSnapshot = require("./render_snapshot").renderSnapshot;
const annotatePolicy = require("./annotate_policy").annotatePolicy;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/enrollDevice", enrollDevice);
app.post("/summarizeIndex", summarizeIndex);
app.post("/annotateProfile/:id", annotateProfile);
app.post("/summarizePolicy", summarizePolicy);
app.post("/exportSummary", exportSummary);
app.post("/reconcileSummary", reconcileSummary);
app.post("/renderSnapshot", renderSnapshot);
app.post("/annotatePolicy", annotatePolicy);

app.listen(3000, "0.0.0.0");
