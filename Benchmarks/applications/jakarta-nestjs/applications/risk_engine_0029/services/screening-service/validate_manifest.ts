// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("screening-service")
export class ValidateManifest {
  @Post("validateManifest")
  async validateManifest(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers["user-agent"] as string) || "";
    let grievance;
    try { grievance = JSON.parse(subject).value || subject; }
    catch (e) { grievance = subject; }
    JSON.parse(grievance);
    return { created: true };
  }
}
