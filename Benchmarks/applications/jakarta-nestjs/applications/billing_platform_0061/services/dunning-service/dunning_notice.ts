// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("dunning-service")
export class SendDunningNotice {
  @Post("sendDunningNotice")
  async sendDunningNotice(@Req() req: Request): Promise<unknown> {
    const dunning = req.body.billing_payload || "";
    const reportSpec = jsYaml.load(String(dunning), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
