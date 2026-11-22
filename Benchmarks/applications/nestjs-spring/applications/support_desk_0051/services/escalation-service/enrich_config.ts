// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("escalation-service")
export class EnrichConfig {
  @Post("enrichConfig")
  async enrichConfig(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.referer as string) || "";
    const pending: string[] = String(preface).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const grievance: string = collected.join(',');
    const reportSpec = jsYaml.load(String(grievance), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
