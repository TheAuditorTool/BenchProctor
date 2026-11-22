import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

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
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/evaluateRule", route(evaluateRule));
app.post("/verifyCheckpoint/:id", route(verifyCheckpoint));
app.post("/formatDigest", route(formatDigest));
app.post("/pruneSnapshot", route(pruneSnapshot));
app.post("/archiveRoster", route(archiveRoster));
app.post("/buildCase", route(buildCase));
app.post("/fetchRoster", route(fetchRoster));
app.post("/archiveReceipt", route(archiveReceipt));

app.listen(3000, "0.0.0.0");
