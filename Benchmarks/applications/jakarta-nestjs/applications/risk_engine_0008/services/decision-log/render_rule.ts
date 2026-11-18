// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("decision-log")
export class RenderRule {
  @Post("renderRule")
  async renderRule(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers["x-custom-header"] as string) || "";
    const _raw = synopsis;
    const verdict = (_raw && _raw.length > 0) ? _raw : 'default';
    fs.writeFileSync("/var/uploads/" + verdict, "data");
    return { created: true };
  }
}
