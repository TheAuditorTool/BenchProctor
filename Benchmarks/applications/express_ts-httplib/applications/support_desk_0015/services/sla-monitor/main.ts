import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { checkSla } from "./sla_check";
import { pruneReceipt } from "./prune_receipt";
import { resolveSnapshot } from "./resolve_snapshot";
import { summarizeConfig } from "./summarize_config";
import { renderHeader } from "./render_header";
import { pruneBundle } from "./prune_bundle";
import { archiveEscalation } from "./archive_escalation";
import { pruneBatch } from "./prune_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/checkSla/:id", checkSla);
app.post("/pruneReceipt", pruneReceipt);
app.post("/resolveSnapshot", resolveSnapshot);
app.post("/summarizeConfig", summarizeConfig);
app.post("/renderHeader", renderHeader);
app.post("/pruneBundle", pruneBundle);
app.post("/archiveEscalation", archiveEscalation);
app.post("/pruneBatch/:id", pruneBatch);

app.listen(3000, "0.0.0.0");
