const express = require("express");
const session = require("express-session");

const indexMetadata = require("./metadata_index").indexMetadata;
const buildLedger = require("./build_ledger").buildLedger;
const enrichWindow = require("./enrich_window").enrichWindow;
const formatCheckpoint = require("./format_checkpoint").formatCheckpoint;
const reconcileProfile = require("./reconcile_profile").reconcileProfile;
const archiveHeader = require("./archive_header").archiveHeader;
const loadReport = require("./load_report").loadReport;
const fetchWindow = require("./fetch_window").fetchWindow;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/indexMetadata", route(indexMetadata));
app.post("/buildLedger", route(buildLedger));
app.post("/enrichWindow", route(enrichWindow));
app.post("/formatCheckpoint", route(formatCheckpoint));
app.post("/reconcileProfile/:id", route(reconcileProfile));
app.post("/archiveHeader", route(archiveHeader));
app.post("/loadReport", route(loadReport));
app.post("/fetchWindow", route(fetchWindow));

app.listen(3000, "0.0.0.0");
