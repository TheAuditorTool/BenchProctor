import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { configureSample } from "./sample_config";
import { pruneDigest } from "./prune_digest";
import { compactManifest } from "./compact_manifest";
import { exportRoster } from "./export_roster";
import { verifyThreshold } from "./verify_threshold";
import { validateRecord } from "./validate_record";
import { pruneCheckpoint } from "./prune_checkpoint";
import { exportHeader } from "./export_header";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/configureSample", route(configureSample));
app.post("/pruneDigest", route(pruneDigest));
app.post("/compactManifest", route(compactManifest));
app.post("/exportRoster", route(exportRoster));
app.post("/verifyThreshold", route(verifyThreshold));
app.post("/validateRecord", route(validateRecord));
app.post("/pruneCheckpoint", route(pruneCheckpoint));
app.post("/exportHeader", route(exportHeader));

app.listen(3000, "0.0.0.0");
