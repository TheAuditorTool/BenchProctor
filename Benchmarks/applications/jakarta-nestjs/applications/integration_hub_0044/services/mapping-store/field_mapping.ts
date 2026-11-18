// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("mapping-store")
export class MapField {
  @Post("mapField")
  async mapField(@Req() req: Request): Promise<unknown> {
    const headline = req.body.integrations_payload || "";
    childProcess.execFileSync("echo", [headline]);
    return { created: true };
  }
}
