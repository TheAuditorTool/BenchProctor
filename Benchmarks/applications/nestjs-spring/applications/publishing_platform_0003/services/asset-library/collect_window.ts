// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("asset-library")
export class CollectWindow {
  @Post("collectWindow")
  async collectWindow(@Req() req: Request): Promise<unknown> {
    const heading = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(heading).split(',')) { parts.push(token); }
    const addendum: string = parts.join(',');
    const reportSpec = jsYaml.load(String(addendum), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
