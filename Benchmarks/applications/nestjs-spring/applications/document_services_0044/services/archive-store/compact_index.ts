// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Controller("archive-store")
export class CompactIndex {
  @Post("compactIndex")
  async compactIndex(@Req() req: Request): Promise<unknown> {
    const phrase = (req.query.id as string) || "";
    const dossier = phrase != null ? phrase : '';
    const reportSpec = jsYaml.load(String(dossier), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
