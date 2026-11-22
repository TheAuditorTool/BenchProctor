import express, { Request, Response } from "express";
import session from "express-session";

import { evaluateRule } from "./rule_evaluate";
import { verifyCheckpoint } from "./verify_checkpoint";
import { formatDigest } from "./format_digest";
import { pruneSnapshot } from "./prune_snapshot";
import { archiveRoster } from "./archive_roster";
import { buildCase } from "./build_case";
import { fetchRoster } from "./fetch_roster";
import { archiveReceipt } from "./archive_receipt";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/evaluateRule", evaluateRule);
app.post("/verifyCheckpoint", verifyCheckpoint);
app.post("/formatDigest", formatDigest);
app.post("/pruneSnapshot", pruneSnapshot);
app.post("/archiveRoster", archiveRoster);
app.post("/buildCase", buildCase);
app.post("/fetchRoster/:id", fetchRoster);
app.post("/archiveReceipt", archiveReceipt);

app.listen(3000, "0.0.0.0");
