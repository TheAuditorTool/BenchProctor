// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import * as nodeSerialize from "node-serialize";

@Controller("capture-service")
export class FormatReport {
  @Post("formatReport")
  async formatReport(@Req() req: Request): Promise<unknown> {
    const caption = (await shared.mq.receive("app-events"));
    const formData = Object.freeze({ payload: caption });
    const ledger = formData.payload;
    nodeSerialize.unserialize(ledger);
    return { created: true };
  }
}
