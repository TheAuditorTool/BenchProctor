// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("macro-service")
export class NormalizeProfile {
  @Post("normalizeProfile")
  async normalizeProfile(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(preface);
    let grievance;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': grievance = _input.normalize('NFC'); break;
      default: grievance = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + grievance, "data");
    return { created: true };
  }
}
