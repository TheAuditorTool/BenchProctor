// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("release-api")
export class BuildSummary {
  @Post("buildSummary")
  async buildSummary(@Req() req: Request): Promise<unknown> {
    const summary = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const phrase: string = parts.join(',');
    const reportSpec = jsYaml.load(String(phrase), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
