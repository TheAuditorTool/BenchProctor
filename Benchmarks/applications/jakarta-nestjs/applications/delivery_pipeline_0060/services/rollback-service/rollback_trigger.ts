// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("rollback-service")
export class TriggerRollback {
  @Post("triggerRollback")
  async triggerRollback(@Req() req: Request): Promise<unknown> {
    const subtitle = req.body.delivery_payload || "";
    nodeSerialize.unserialize(subtitle);
    return { created: true };
  }
}
