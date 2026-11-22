// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("device-trust")
export class ExportSummary {
  @Post("exportSummary")
  async exportSummary(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers.referer as string) || "";
    const pending: string[] = String(paragraph).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const persona: string = collected.join(',');
    const reportSpec = jsYaml.load(String(persona), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
