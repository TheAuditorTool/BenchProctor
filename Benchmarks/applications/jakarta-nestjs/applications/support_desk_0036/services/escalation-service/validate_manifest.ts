// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("escalation-service")
export class ValidateManifest {
  @Post("validateManifest")
  async validateManifest(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.host as string) || "";
    const [grievance] = String(preface).split(',');
    http.get(grievance);
    return { created: true };
  }
}
