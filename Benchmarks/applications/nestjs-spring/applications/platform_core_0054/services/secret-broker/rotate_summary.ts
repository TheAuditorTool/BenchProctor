// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("secret-broker")
export class RotateSummary {
  @Post("rotateSummary/:id")
  async rotateSummary(@Req() req: Request): Promise<unknown> {
    const snippet = (req.params.id as string) || "";
    let persona;
    try { persona = JSON.parse(snippet).value || snippet; }
    catch (e) { persona = snippet; }
    fs.unlinkSync("/var/app/data/" + persona);
    return { created: true };
  }
}
