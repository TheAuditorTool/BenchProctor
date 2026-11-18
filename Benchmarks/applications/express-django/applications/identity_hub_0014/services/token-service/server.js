const express = require("express");
const session = require("express-session");

const mintToken = require("./token_mint").mintToken;
const exportIndex = require("./export_index").exportIndex;
const enrichManifest = require("./enrich_manifest").enrichManifest;
const exportHeader = require("./export_header").exportHeader;
const compactLedger = require("./compact_ledger").compactLedger;
const fetchManifest = require("./fetch_manifest").fetchManifest;
const mergeManifest = require("./merge_manifest").mergeManifest;
const fetchRoster = require("./fetch_roster").fetchRoster;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/mintToken/:id", route(mintToken));
app.post("/exportIndex", route(exportIndex));
app.post("/enrichManifest", route(enrichManifest));
app.post("/exportHeader", route(exportHeader));
app.post("/compactLedger", route(compactLedger));
app.post("/fetchManifest", route(fetchManifest));
app.post("/mergeManifest", route(mergeManifest));
app.post("/fetchRoster", route(fetchRoster));

app.listen(3000, "0.0.0.0");
