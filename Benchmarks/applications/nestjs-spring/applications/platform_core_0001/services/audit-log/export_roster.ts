// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import * as nodeSerialize from "node-serialize";

@Controller("audit-log")
export class ExportRoster {
  @Post("exportRoster")
  async exportRoster(@Req() req: Request): Promise<unknown> {
    const tagline = (await shared.mq.receive("app-events"));
    const formData = Object.freeze({ payload: tagline });
    const persona = formData.payload;
    nodeSerialize.unserialize(persona);
    return { created: true };
  }
}
