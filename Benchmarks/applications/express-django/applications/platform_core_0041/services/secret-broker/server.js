const express = require("express");
const session = require("express-session");

const fetchSecret = require("./secret_fetch").fetchSecret;
const collectRecord = require("./collect_record").collectRecord;
const normalizeFlag = require("./normalize_flag").normalizeFlag;
const archiveDigest = require("./archive_digest").archiveDigest;
const reconcileConfig = require("./reconcile_config").reconcileConfig;
const publishQuota = require("./publish_quota").publishQuota;
const normalizeRoster = require("./normalize_roster").normalizeRoster;
const resolveBatch = require("./resolve_batch").resolveBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/fetchSecret", route(fetchSecret));
app.post("/collectRecord", route(collectRecord));
app.post("/normalizeFlag", route(normalizeFlag));
app.post("/archiveDigest", route(archiveDigest));
app.post("/reconcileConfig", route(reconcileConfig));
app.post("/publishQuota", route(publishQuota));
app.post("/normalizeRoster", route(normalizeRoster));
app.post("/resolveBatch", route(resolveBatch));

app.listen(3000, "0.0.0.0");
