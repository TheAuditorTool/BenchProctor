// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00189")
  async BenchmarkTest00189(@Headers("host") host: string): Promise<unknown> {
    const userInput = host || "";
    const payload = { get value() { return userInput; } };
    const data = payload.value;
    const emailMatch = String(data).match(/@([A-Za-z0-9.-]+)$/);
    if (!emailMatch) { throw new BadRequestException({ error: "not an email address" }); }
    const domain = emailMatch[1];
    return { domain };
  }
}
