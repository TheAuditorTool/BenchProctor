import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { storeArchive } from "./archive_store";
import { auditIndex } from "./audit_index";
import { archiveDigest } from "./archive_digest";
import { publishManifest } from "./publish_manifest";
import { buildProfile } from "./build_profile";
import { validateCheckpoint } from "./validate_checkpoint";
import { reconcileCheckpoint } from "./reconcile_checkpoint";
import { resolveRoster } from "./resolve_roster";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/storeArchive", route(storeArchive));
app.post("/auditIndex", route(auditIndex));
app.post("/archiveDigest", route(archiveDigest));
app.post("/publishManifest", route(publishManifest));
app.post("/buildProfile", route(buildProfile));
app.post("/validateCheckpoint", route(validateCheckpoint));
app.post("/reconcileCheckpoint/:id", route(reconcileCheckpoint));
app.post("/resolveRoster", route(resolveRoster));

app.listen(3000, "0.0.0.0");
