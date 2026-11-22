// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("sampling-config")
export class ConfigureSample {
  @Post("configureSample")
  async configureSample(@Req() req: Request): Promise<unknown> {
    const blurb = req.body.telemetry_payload || "";
    nodeSerialize.unserialize(blurb);
    return { created: true };
  }
}
