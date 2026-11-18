const express = require("express");
const session = require("express-session");

const postComment = require("./comment_post").postComment;
const rotateSchedule = require("./rotate_schedule").rotateSchedule;
const buildPolicy = require("./build_policy").buildPolicy;
const normalizeDocument = require("./normalize_document").normalizeDocument;
const validateBundle = require("./validate_bundle").validateBundle;
const summarizeRecord = require("./summarize_record").summarizeRecord;
const validateWorkspace = require("./validate_workspace").validateWorkspace;
const pruneBatch = require("./prune_batch").pruneBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/postComment", route(postComment));
app.post("/rotateSchedule", route(rotateSchedule));
app.post("/buildPolicy", route(buildPolicy));
app.post("/normalizeDocument", route(normalizeDocument));
app.post("/validateBundle", route(validateBundle));
app.post("/summarizeRecord", route(summarizeRecord));
app.post("/validateWorkspace", route(validateWorkspace));
app.post("/pruneBatch", route(pruneBatch));

app.listen(3000, "0.0.0.0");
