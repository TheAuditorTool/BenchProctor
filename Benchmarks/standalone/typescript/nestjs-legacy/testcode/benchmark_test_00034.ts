// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Header, Post } from "@nestjs/common";
import { Response } from "express";
import * as nunjucks from "nunjucks";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00034")
  @Header("Content-Type", "text/html")
  async BenchmarkTest00034(@Body("field") field: string): Promise<unknown> {
    const userInput = field || "";
    const data = String(userInput).split(/[ \t]+/).join(" ");
    const processed = data.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: processed });
    return page;
  }
}
