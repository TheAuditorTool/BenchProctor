// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("release-api")
export class CutRelease {
  @Post("cutRelease")
  async cutRelease(@Req() req: Request): Promise<unknown> {
    const summary = fs.readFileSync("/tmp/data", "utf8");
    const phrase = Buffer.from(summary, "base64").toString();
    await fetch("http://rollback-service:8080/TriggerRollback", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: phrase})});
    return { created: true };
  }
}
