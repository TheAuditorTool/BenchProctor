// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("sla-monitor")
export class ValidateProfile {
  @Post("validateProfile")
  async validateProfile(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["user-agent"] as string) || "";
    let grievance;
    try { grievance = JSON.parse(preface).value || preface; }
    catch (e) { grievance = preface; }
    const inquiry = "/var/app/data/" + path.basename(grievance);
    const fileContent = fs.readFileSync(inquiry, "utf8");
    return fileContent;
  }
}
