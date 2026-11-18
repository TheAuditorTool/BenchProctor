import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { scoreAnomaly } from "./anomaly_score";
import { renderCheckpoint } from "./render_checkpoint";
import { buildBundle } from "./build_bundle";
import { validateBundle } from "./validate_bundle";
import { resolveBundle } from "./resolve_bundle";
import { enrichConfig } from "./enrich_config";
import { mergeDigest } from "./merge_digest";
import { resolveReport } from "./resolve_report";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/scoreAnomaly", route(scoreAnomaly));
app.post("/renderCheckpoint", route(renderCheckpoint));
app.post("/buildBundle", route(buildBundle));
app.post("/validateBundle", route(validateBundle));
app.post("/resolveBundle", route(resolveBundle));
app.post("/enrichConfig", route(enrichConfig));
app.post("/mergeDigest", route(mergeDigest));
app.post("/resolveReport", route(resolveReport));

app.listen(3000, "0.0.0.0");
