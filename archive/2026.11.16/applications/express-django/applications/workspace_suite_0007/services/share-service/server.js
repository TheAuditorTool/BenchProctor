const express = require("express");
const session = require("express-session");

const grantShare = require("./share_grant").grantShare;
const renderPolicy = require("./render_policy").renderPolicy;
const publishRecord = require("./publish_record").publishRecord;
const loadBundle = require("./load_bundle").loadBundle;
const pruneConfig = require("./prune_config").pruneConfig;
const enrichWorkspace = require("./enrich_workspace").enrichWorkspace;
const enrichManifest = require("./enrich_manifest").enrichManifest;
const annotateRoster = require("./annotate_roster").annotateRoster;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/grantShare", route(grantShare));
app.post("/renderPolicy", route(renderPolicy));
app.post("/publishRecord", route(publishRecord));
app.post("/loadBundle", route(loadBundle));
app.post("/pruneConfig", route(pruneConfig));
app.post("/enrichWorkspace", route(enrichWorkspace));
app.post("/enrichManifest", route(enrichManifest));
app.post("/annotateRoster", route(annotateRoster));

app.listen(3000, "0.0.0.0");
