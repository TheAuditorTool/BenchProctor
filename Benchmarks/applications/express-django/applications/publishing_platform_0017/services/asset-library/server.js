const express = require("express");
const session = require("express-session");

const attachAsset = require("./asset_attach").attachAsset;
const collectSyndication = require("./collect_syndication").collectSyndication;
const fetchBatch = require("./fetch_batch").fetchBatch;
const enrichConfig = require("./enrich_config").enrichConfig;
const reconcileWindow = require("./reconcile_window").reconcileWindow;
const renderIndex = require("./render_index").renderIndex;
const summarizeLedger = require("./summarize_ledger").summarizeLedger;
const archiveConfig = require("./archive_config").archiveConfig;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/attachAsset", route(attachAsset));
app.post("/collectSyndication", route(collectSyndication));
app.post("/fetchBatch/:id", route(fetchBatch));
app.post("/enrichConfig", route(enrichConfig));
app.post("/reconcileWindow", route(reconcileWindow));
app.post("/renderIndex", route(renderIndex));
app.post("/summarizeLedger", route(summarizeLedger));
app.post("/archiveConfig", route(archiveConfig));

app.listen(3000, "0.0.0.0");
