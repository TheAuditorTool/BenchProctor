const express = require("express");
const session = require("express-session");

const queryDashboard = require("./dashboard_query").queryDashboard;
const pruneLedger = require("./prune_ledger").pruneLedger;
const resolveHeader = require("./resolve_header").resolveHeader;
const enrichIndex = require("./enrich_index").enrichIndex;
const collectBundle = require("./collect_bundle").collectBundle;
const collectReport = require("./collect_report").collectReport;
const annotateRecord = require("./annotate_record").annotateRecord;
const formatDigest = require("./format_digest").formatDigest;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/queryDashboard", route(queryDashboard));
app.post("/pruneLedger", route(pruneLedger));
app.post("/resolveHeader", route(resolveHeader));
app.post("/enrichIndex", route(enrichIndex));
app.post("/collectBundle", route(collectBundle));
app.post("/collectReport", route(collectReport));
app.post("/annotateRecord", route(annotateRecord));
app.post("/formatDigest", route(formatDigest));

app.listen(3000, "0.0.0.0");
