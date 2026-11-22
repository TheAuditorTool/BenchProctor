const express = require("express");
const session = require("express-session");

const rollDigest = require("./digest_roll").rollDigest;
const compactChannel = require("./compact_channel").compactChannel;
const resolveConfig = require("./resolve_config").resolveConfig;
const pruneSchedule = require("./prune_schedule").pruneSchedule;
const renderProfile = require("./render_profile").renderProfile;
const loadPolicy = require("./load_policy").loadPolicy;
const enrichConfig = require("./enrich_config").enrichConfig;
const archiveConfig = require("./archive_config").archiveConfig;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/rollDigest", route(rollDigest));
app.post("/compactChannel", route(compactChannel));
app.post("/resolveConfig", route(resolveConfig));
app.post("/pruneSchedule", route(pruneSchedule));
app.post("/renderProfile", route(renderProfile));
app.post("/loadPolicy", route(loadPolicy));
app.post("/enrichConfig", route(enrichConfig));
app.post("/archiveConfig", route(archiveConfig));

app.listen(3000, "0.0.0.0");
