import express, { Request, Response } from "express";
import session from "express-session";

import { checkSla } from "./sla_check";
import { auditSurvey } from "./audit_survey";
import { resolveWindow } from "./resolve_window";
import { validateProfile } from "./validate_profile";
import { auditPolicy } from "./audit_policy";
import { summarizeRoster } from "./summarize_roster";
import { archiveBundle } from "./archive_bundle";
import { rotateMacro } from "./rotate_macro";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/checkSla", checkSla);
app.post("/auditSurvey", auditSurvey);
app.post("/resolveWindow/:id", resolveWindow);
app.post("/validateProfile", validateProfile);
app.post("/auditPolicy", auditPolicy);
app.post("/summarizeRoster/:id", summarizeRoster);
app.post("/archiveBundle", archiveBundle);
app.post("/rotateMacro", rotateMacro);

app.listen(3000, "0.0.0.0");
