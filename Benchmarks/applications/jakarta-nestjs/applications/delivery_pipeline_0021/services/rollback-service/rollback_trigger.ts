// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("rollback-service")
export class TriggerRollback {
  @Post("triggerRollback")
  async triggerRollback(@Req() req: Request): Promise<unknown> {
    const passage = req.body.delivery_payload || "";
    fs.writeFileSync("/var/uploads/" + passage, "data");
    return { created: true };
  }
}
