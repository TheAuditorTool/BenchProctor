// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, Redirect } from "@nestjs/common";
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
  @Post("BenchmarkTest00290")
  @Redirect()
  async BenchmarkTest00290(@Body("variables") vars: { input?: string }): Promise<unknown> {
    const userInput = (vars?.input as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const data: string = normalize(userInput);
    return { url: data };
  }
}
