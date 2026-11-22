const express = require("express");
const session = require("express-session");

const renderPreview = require("./preview_render").renderPreview;
const renderLedger = require("./render_ledger").renderLedger;
const loadConfig = require("./load_config").loadConfig;
const loadRoster = require("./load_roster").loadRoster;
const renderSnapshot = require("./render_snapshot").renderSnapshot;
const compactLedger = require("./compact_ledger").compactLedger;
const annotateRecord = require("./annotate_record").annotateRecord;
const formatRevision = require("./format_revision").formatRevision;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/renderPreview/:id", renderPreview);
app.post("/renderLedger", renderLedger);
app.post("/loadConfig", loadConfig);
app.post("/loadRoster", loadRoster);
app.post("/renderSnapshot", renderSnapshot);
app.post("/compactLedger", compactLedger);
app.post("/annotateRecord", annotateRecord);
app.post("/formatRevision", formatRevision);

app.listen(3000, "0.0.0.0");
