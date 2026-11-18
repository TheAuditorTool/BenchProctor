const express = require("express");
const session = require("express-session");

const uploadAsset = require("./asset_upload").uploadAsset;
const buildSnapshot = require("./build_snapshot").buildSnapshot;
const buildHeader = require("./build_header").buildHeader;
const mergeIndex = require("./merge_index").mergeIndex;
const fetchWindow = require("./fetch_window").fetchWindow;
const loadPolicy = require("./load_policy").loadPolicy;
const pruneLedger = require("./prune_ledger").pruneLedger;
const formatManifest = require("./format_manifest").formatManifest;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/uploadAsset", route(uploadAsset));
app.post("/buildSnapshot", route(buildSnapshot));
app.post("/buildHeader", route(buildHeader));
app.post("/mergeIndex", route(mergeIndex));
app.post("/fetchWindow", route(fetchWindow));
app.post("/loadPolicy", route(loadPolicy));
app.post("/pruneLedger", route(pruneLedger));
app.post("/formatManifest", route(formatManifest));

app.listen(3000, "0.0.0.0");
